from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.entities_collection import EntitiesCollection
from ...models.list_entities_response_400 import ListEntitiesResponse400
from ...models.list_entities_response_401 import ListEntitiesResponse401
from ...models.list_entities_response_403 import ListEntitiesResponse403
from ...models.list_entities_response_404 import ListEntitiesResponse404
from ...models.list_entities_response_500 import ListEntitiesResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    platform: Union[Unset, str] = UNSET,
    owners: Union[Unset, str] = UNSET,
    exposure: Union[Unset, str] = UNSET,
    asset_type: Union[Unset, str] = UNSET,
    mime_type: Union[Unset, str] = UNSET,
    updated_before: Union[Unset, str] = UNSET,
    updated_after: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["platform"] = platform

    params["owners"] = owners

    params["exposure"] = exposure

    params["asset_type"] = asset_type

    params["mime_type"] = mime_type

    params["updated_before"] = updated_before

    params["updated_after"] = updated_after

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/entities",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        ListEntitiesResponse400,
        ListEntitiesResponse401,
        ListEntitiesResponse403,
        ListEntitiesResponse404,
        ListEntitiesResponse500,
        list["EntitiesCollection"],
    ]
]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = EntitiesCollection.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = ListEntitiesResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = ListEntitiesResponse401.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = ListEntitiesResponse403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = ListEntitiesResponse404.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = ListEntitiesResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        ListEntitiesResponse400,
        ListEntitiesResponse401,
        ListEntitiesResponse403,
        ListEntitiesResponse404,
        ListEntitiesResponse500,
        list["EntitiesCollection"],
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
    platform: Union[Unset, str] = UNSET,
    owners: Union[Unset, str] = UNSET,
    exposure: Union[Unset, str] = UNSET,
    asset_type: Union[Unset, str] = UNSET,
    mime_type: Union[Unset, str] = UNSET,
    updated_before: Union[Unset, str] = UNSET,
    updated_after: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        ListEntitiesResponse400,
        ListEntitiesResponse401,
        ListEntitiesResponse403,
        ListEntitiesResponse404,
        ListEntitiesResponse500,
        list["EntitiesCollection"],
    ]
]:
    """List Entities

     Get the data for the asset list page and asset list exports. This endpoint requires the Entity Cache
    feature. If you do not have this feature enabled, refer to the incident entitites endpoint as an
    alternative.

    Args:
        platform (Union[Unset, str]):
        owners (Union[Unset, str]):
        exposure (Union[Unset, str]):
        asset_type (Union[Unset, str]):
        mime_type (Union[Unset, str]):
        updated_before (Union[Unset, str]):
        updated_after (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ListEntitiesResponse400, ListEntitiesResponse401, ListEntitiesResponse403, ListEntitiesResponse404, ListEntitiesResponse500, list['EntitiesCollection']]]
    """

    kwargs = _get_kwargs(
        platform=platform,
        owners=owners,
        exposure=exposure,
        asset_type=asset_type,
        mime_type=mime_type,
        updated_before=updated_before,
        updated_after=updated_after,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    platform: Union[Unset, str] = UNSET,
    owners: Union[Unset, str] = UNSET,
    exposure: Union[Unset, str] = UNSET,
    asset_type: Union[Unset, str] = UNSET,
    mime_type: Union[Unset, str] = UNSET,
    updated_before: Union[Unset, str] = UNSET,
    updated_after: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        ListEntitiesResponse400,
        ListEntitiesResponse401,
        ListEntitiesResponse403,
        ListEntitiesResponse404,
        ListEntitiesResponse500,
        list["EntitiesCollection"],
    ]
]:
    """List Entities

     Get the data for the asset list page and asset list exports. This endpoint requires the Entity Cache
    feature. If you do not have this feature enabled, refer to the incident entitites endpoint as an
    alternative.

    Args:
        platform (Union[Unset, str]):
        owners (Union[Unset, str]):
        exposure (Union[Unset, str]):
        asset_type (Union[Unset, str]):
        mime_type (Union[Unset, str]):
        updated_before (Union[Unset, str]):
        updated_after (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ListEntitiesResponse400, ListEntitiesResponse401, ListEntitiesResponse403, ListEntitiesResponse404, ListEntitiesResponse500, list['EntitiesCollection']]
    """

    return sync_detailed(
        client=client,
        platform=platform,
        owners=owners,
        exposure=exposure,
        asset_type=asset_type,
        mime_type=mime_type,
        updated_before=updated_before,
        updated_after=updated_after,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    platform: Union[Unset, str] = UNSET,
    owners: Union[Unset, str] = UNSET,
    exposure: Union[Unset, str] = UNSET,
    asset_type: Union[Unset, str] = UNSET,
    mime_type: Union[Unset, str] = UNSET,
    updated_before: Union[Unset, str] = UNSET,
    updated_after: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        ListEntitiesResponse400,
        ListEntitiesResponse401,
        ListEntitiesResponse403,
        ListEntitiesResponse404,
        ListEntitiesResponse500,
        list["EntitiesCollection"],
    ]
]:
    """List Entities

     Get the data for the asset list page and asset list exports. This endpoint requires the Entity Cache
    feature. If you do not have this feature enabled, refer to the incident entitites endpoint as an
    alternative.

    Args:
        platform (Union[Unset, str]):
        owners (Union[Unset, str]):
        exposure (Union[Unset, str]):
        asset_type (Union[Unset, str]):
        mime_type (Union[Unset, str]):
        updated_before (Union[Unset, str]):
        updated_after (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ListEntitiesResponse400, ListEntitiesResponse401, ListEntitiesResponse403, ListEntitiesResponse404, ListEntitiesResponse500, list['EntitiesCollection']]]
    """

    kwargs = _get_kwargs(
        platform=platform,
        owners=owners,
        exposure=exposure,
        asset_type=asset_type,
        mime_type=mime_type,
        updated_before=updated_before,
        updated_after=updated_after,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    platform: Union[Unset, str] = UNSET,
    owners: Union[Unset, str] = UNSET,
    exposure: Union[Unset, str] = UNSET,
    asset_type: Union[Unset, str] = UNSET,
    mime_type: Union[Unset, str] = UNSET,
    updated_before: Union[Unset, str] = UNSET,
    updated_after: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        ListEntitiesResponse400,
        ListEntitiesResponse401,
        ListEntitiesResponse403,
        ListEntitiesResponse404,
        ListEntitiesResponse500,
        list["EntitiesCollection"],
    ]
]:
    """List Entities

     Get the data for the asset list page and asset list exports. This endpoint requires the Entity Cache
    feature. If you do not have this feature enabled, refer to the incident entitites endpoint as an
    alternative.

    Args:
        platform (Union[Unset, str]):
        owners (Union[Unset, str]):
        exposure (Union[Unset, str]):
        asset_type (Union[Unset, str]):
        mime_type (Union[Unset, str]):
        updated_before (Union[Unset, str]):
        updated_after (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ListEntitiesResponse400, ListEntitiesResponse401, ListEntitiesResponse403, ListEntitiesResponse404, ListEntitiesResponse500, list['EntitiesCollection']]
    """

    return (
        await asyncio_detailed(
            client=client,
            platform=platform,
            owners=owners,
            exposure=exposure,
            asset_type=asset_type,
            mime_type=mime_type,
            updated_before=updated_before,
            updated_after=updated_after,
        )
    ).parsed
