from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_policies_response_400 import ListPoliciesResponse400
from ...models.list_policies_response_401 import ListPoliciesResponse401
from ...models.list_policies_response_403 import ListPoliciesResponse403
from ...models.list_policies_response_404 import ListPoliciesResponse404
from ...models.list_policies_response_500 import ListPoliciesResponse500
from ...models.policies_collection import PoliciesCollection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    state: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["state"] = state

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/policies",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        ListPoliciesResponse400,
        ListPoliciesResponse401,
        ListPoliciesResponse403,
        ListPoliciesResponse404,
        ListPoliciesResponse500,
        list["PoliciesCollection"],
    ]
]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = PoliciesCollection.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = ListPoliciesResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = ListPoliciesResponse401.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = ListPoliciesResponse403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = ListPoliciesResponse404.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = ListPoliciesResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        ListPoliciesResponse400,
        ListPoliciesResponse401,
        ListPoliciesResponse403,
        ListPoliciesResponse404,
        ListPoliciesResponse500,
        list["PoliciesCollection"],
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    state: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        ListPoliciesResponse400,
        ListPoliciesResponse401,
        ListPoliciesResponse403,
        ListPoliciesResponse404,
        ListPoliciesResponse500,
        list["PoliciesCollection"],
    ]
]:
    """List the Organization's Policies

     Get all of the organization's configured policies.

    Args:
        state (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ListPoliciesResponse400, ListPoliciesResponse401, ListPoliciesResponse403, ListPoliciesResponse404, ListPoliciesResponse500, list['PoliciesCollection']]]
    """

    kwargs = _get_kwargs(
        state=state,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    state: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        ListPoliciesResponse400,
        ListPoliciesResponse401,
        ListPoliciesResponse403,
        ListPoliciesResponse404,
        ListPoliciesResponse500,
        list["PoliciesCollection"],
    ]
]:
    """List the Organization's Policies

     Get all of the organization's configured policies.

    Args:
        state (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ListPoliciesResponse400, ListPoliciesResponse401, ListPoliciesResponse403, ListPoliciesResponse404, ListPoliciesResponse500, list['PoliciesCollection']]
    """

    return sync_detailed(
        client=client,
        state=state,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    state: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        ListPoliciesResponse400,
        ListPoliciesResponse401,
        ListPoliciesResponse403,
        ListPoliciesResponse404,
        ListPoliciesResponse500,
        list["PoliciesCollection"],
    ]
]:
    """List the Organization's Policies

     Get all of the organization's configured policies.

    Args:
        state (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ListPoliciesResponse400, ListPoliciesResponse401, ListPoliciesResponse403, ListPoliciesResponse404, ListPoliciesResponse500, list['PoliciesCollection']]]
    """

    kwargs = _get_kwargs(
        state=state,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    state: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        ListPoliciesResponse400,
        ListPoliciesResponse401,
        ListPoliciesResponse403,
        ListPoliciesResponse404,
        ListPoliciesResponse500,
        list["PoliciesCollection"],
    ]
]:
    """List the Organization's Policies

     Get all of the organization's configured policies.

    Args:
        state (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ListPoliciesResponse400, ListPoliciesResponse401, ListPoliciesResponse403, ListPoliciesResponse404, ListPoliciesResponse500, list['PoliciesCollection']]
    """

    return (
        await asyncio_detailed(
            client=client,
            state=state,
        )
    ).parsed
