from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.common_rest_error import CommonRestError
from ...models.config_fabric_vni_members_response import ConfigFabricVniMembersResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    fabric_id: str,
    vni_id: str,
    *,
    candidate: Union[Unset, str] = UNSET,
    include_metadata: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["candidate"] = candidate

    params["includeMetadata"] = include_metadata

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/fabrics/{fabric_id}/vnis/{vni_id}/members",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CommonRestError, ConfigFabricVniMembersResponse]]:
    if response.status_code == 200:
        response_200 = ConfigFabricVniMembersResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = CommonRestError.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = CommonRestError.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = CommonRestError.from_dict(response.json())

        return response_403
    if response.status_code == 429:
        response_429 = CommonRestError.from_dict(response.json())

        return response_429
    if response.status_code == 500:
        response_500 = CommonRestError.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[CommonRestError, ConfigFabricVniMembersResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    fabric_id: str,
    vni_id: str,
    *,
    client: AuthenticatedClient,
    candidate: Union[Unset, str] = UNSET,
    include_metadata: Union[Unset, bool] = UNSET,
) -> Response[Union[CommonRestError, ConfigFabricVniMembersResponse]]:
    """Get the list of VNI members.

     Get the list of members of a specific VNI in a fabric.

    Args:
        fabric_id (str):
        vni_id (str):
        candidate (Union[Unset, str]):
        include_metadata (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CommonRestError, ConfigFabricVniMembersResponse]]
    """

    kwargs = _get_kwargs(
        fabric_id=fabric_id,
        vni_id=vni_id,
        candidate=candidate,
        include_metadata=include_metadata,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    fabric_id: str,
    vni_id: str,
    *,
    client: AuthenticatedClient,
    candidate: Union[Unset, str] = UNSET,
    include_metadata: Union[Unset, bool] = UNSET,
) -> Optional[Union[CommonRestError, ConfigFabricVniMembersResponse]]:
    """Get the list of VNI members.

     Get the list of members of a specific VNI in a fabric.

    Args:
        fabric_id (str):
        vni_id (str):
        candidate (Union[Unset, str]):
        include_metadata (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CommonRestError, ConfigFabricVniMembersResponse]
    """

    return sync_detailed(
        fabric_id=fabric_id,
        vni_id=vni_id,
        client=client,
        candidate=candidate,
        include_metadata=include_metadata,
    ).parsed


async def asyncio_detailed(
    fabric_id: str,
    vni_id: str,
    *,
    client: AuthenticatedClient,
    candidate: Union[Unset, str] = UNSET,
    include_metadata: Union[Unset, bool] = UNSET,
) -> Response[Union[CommonRestError, ConfigFabricVniMembersResponse]]:
    """Get the list of VNI members.

     Get the list of members of a specific VNI in a fabric.

    Args:
        fabric_id (str):
        vni_id (str):
        candidate (Union[Unset, str]):
        include_metadata (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CommonRestError, ConfigFabricVniMembersResponse]]
    """

    kwargs = _get_kwargs(
        fabric_id=fabric_id,
        vni_id=vni_id,
        candidate=candidate,
        include_metadata=include_metadata,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    fabric_id: str,
    vni_id: str,
    *,
    client: AuthenticatedClient,
    candidate: Union[Unset, str] = UNSET,
    include_metadata: Union[Unset, bool] = UNSET,
) -> Optional[Union[CommonRestError, ConfigFabricVniMembersResponse]]:
    """Get the list of VNI members.

     Get the list of members of a specific VNI in a fabric.

    Args:
        fabric_id (str):
        vni_id (str):
        candidate (Union[Unset, str]):
        include_metadata (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CommonRestError, ConfigFabricVniMembersResponse]
    """

    return (
        await asyncio_detailed(
            fabric_id=fabric_id,
            vni_id=vni_id,
            client=client,
            candidate=candidate,
            include_metadata=include_metadata,
        )
    ).parsed
