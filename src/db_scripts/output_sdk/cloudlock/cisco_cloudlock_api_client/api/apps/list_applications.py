from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.apps_collection import AppsCollection
from ...models.list_applications_response_400 import ListApplicationsResponse400
from ...models.list_applications_response_401 import ListApplicationsResponse401
from ...models.list_applications_response_403 import ListApplicationsResponse403
from ...models.list_applications_response_404 import ListApplicationsResponse404
from ...models.list_applications_response_500 import ListApplicationsResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: Union[Unset, str] = UNSET,
    offset: Union[Unset, str] = UNSET,
    classification: Union[Unset, str] = UNSET,
    vendor: Union[Unset, str] = UNSET,
    app_category: Union[Unset, str] = UNSET,
    detected_at_after: Union[Unset, str] = UNSET,
    detected_at_before: Union[Unset, str] = UNSET,
    app_ids: Union[Unset, str] = UNSET,
    scope_categories: Union[Unset, str] = UNSET,
    install_state: Union[Unset, str] = UNSET,
    count_total: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params["classification"] = classification

    params["vendor"] = vendor

    params["app_category"] = app_category

    params["detected_at_after"] = detected_at_after

    params["detected_at_before"] = detected_at_before

    params["app_ids"] = app_ids

    params["scope_categories"] = scope_categories

    params["install_state"] = install_state

    params["count_total"] = count_total

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/apps",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        ListApplicationsResponse400,
        ListApplicationsResponse401,
        ListApplicationsResponse403,
        ListApplicationsResponse404,
        ListApplicationsResponse500,
        list["AppsCollection"],
    ]
]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AppsCollection.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = ListApplicationsResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = ListApplicationsResponse401.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = ListApplicationsResponse403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = ListApplicationsResponse404.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = ListApplicationsResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        ListApplicationsResponse400,
        ListApplicationsResponse401,
        ListApplicationsResponse403,
        ListApplicationsResponse404,
        ListApplicationsResponse500,
        list["AppsCollection"],
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
    limit: Union[Unset, str] = UNSET,
    offset: Union[Unset, str] = UNSET,
    classification: Union[Unset, str] = UNSET,
    vendor: Union[Unset, str] = UNSET,
    app_category: Union[Unset, str] = UNSET,
    detected_at_after: Union[Unset, str] = UNSET,
    detected_at_before: Union[Unset, str] = UNSET,
    app_ids: Union[Unset, str] = UNSET,
    scope_categories: Union[Unset, str] = UNSET,
    install_state: Union[Unset, str] = UNSET,
    count_total: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        ListApplicationsResponse400,
        ListApplicationsResponse401,
        ListApplicationsResponse403,
        ListApplicationsResponse404,
        ListApplicationsResponse500,
        list["AppsCollection"],
    ]
]:
    """List Applications for the Organization

     Get all of the organization's installed applications and their current status.
    To get the uninstalled applications, use the `install_state` filter.

    Args:
        limit (Union[Unset, str]):
        offset (Union[Unset, str]):
        classification (Union[Unset, str]):
        vendor (Union[Unset, str]):
        app_category (Union[Unset, str]):
        detected_at_after (Union[Unset, str]):
        detected_at_before (Union[Unset, str]):
        app_ids (Union[Unset, str]):
        scope_categories (Union[Unset, str]):
        install_state (Union[Unset, str]):
        count_total (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ListApplicationsResponse400, ListApplicationsResponse401, ListApplicationsResponse403, ListApplicationsResponse404, ListApplicationsResponse500, list['AppsCollection']]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        classification=classification,
        vendor=vendor,
        app_category=app_category,
        detected_at_after=detected_at_after,
        detected_at_before=detected_at_before,
        app_ids=app_ids,
        scope_categories=scope_categories,
        install_state=install_state,
        count_total=count_total,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, str] = UNSET,
    offset: Union[Unset, str] = UNSET,
    classification: Union[Unset, str] = UNSET,
    vendor: Union[Unset, str] = UNSET,
    app_category: Union[Unset, str] = UNSET,
    detected_at_after: Union[Unset, str] = UNSET,
    detected_at_before: Union[Unset, str] = UNSET,
    app_ids: Union[Unset, str] = UNSET,
    scope_categories: Union[Unset, str] = UNSET,
    install_state: Union[Unset, str] = UNSET,
    count_total: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        ListApplicationsResponse400,
        ListApplicationsResponse401,
        ListApplicationsResponse403,
        ListApplicationsResponse404,
        ListApplicationsResponse500,
        list["AppsCollection"],
    ]
]:
    """List Applications for the Organization

     Get all of the organization's installed applications and their current status.
    To get the uninstalled applications, use the `install_state` filter.

    Args:
        limit (Union[Unset, str]):
        offset (Union[Unset, str]):
        classification (Union[Unset, str]):
        vendor (Union[Unset, str]):
        app_category (Union[Unset, str]):
        detected_at_after (Union[Unset, str]):
        detected_at_before (Union[Unset, str]):
        app_ids (Union[Unset, str]):
        scope_categories (Union[Unset, str]):
        install_state (Union[Unset, str]):
        count_total (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ListApplicationsResponse400, ListApplicationsResponse401, ListApplicationsResponse403, ListApplicationsResponse404, ListApplicationsResponse500, list['AppsCollection']]
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        classification=classification,
        vendor=vendor,
        app_category=app_category,
        detected_at_after=detected_at_after,
        detected_at_before=detected_at_before,
        app_ids=app_ids,
        scope_categories=scope_categories,
        install_state=install_state,
        count_total=count_total,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, str] = UNSET,
    offset: Union[Unset, str] = UNSET,
    classification: Union[Unset, str] = UNSET,
    vendor: Union[Unset, str] = UNSET,
    app_category: Union[Unset, str] = UNSET,
    detected_at_after: Union[Unset, str] = UNSET,
    detected_at_before: Union[Unset, str] = UNSET,
    app_ids: Union[Unset, str] = UNSET,
    scope_categories: Union[Unset, str] = UNSET,
    install_state: Union[Unset, str] = UNSET,
    count_total: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        ListApplicationsResponse400,
        ListApplicationsResponse401,
        ListApplicationsResponse403,
        ListApplicationsResponse404,
        ListApplicationsResponse500,
        list["AppsCollection"],
    ]
]:
    """List Applications for the Organization

     Get all of the organization's installed applications and their current status.
    To get the uninstalled applications, use the `install_state` filter.

    Args:
        limit (Union[Unset, str]):
        offset (Union[Unset, str]):
        classification (Union[Unset, str]):
        vendor (Union[Unset, str]):
        app_category (Union[Unset, str]):
        detected_at_after (Union[Unset, str]):
        detected_at_before (Union[Unset, str]):
        app_ids (Union[Unset, str]):
        scope_categories (Union[Unset, str]):
        install_state (Union[Unset, str]):
        count_total (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ListApplicationsResponse400, ListApplicationsResponse401, ListApplicationsResponse403, ListApplicationsResponse404, ListApplicationsResponse500, list['AppsCollection']]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        classification=classification,
        vendor=vendor,
        app_category=app_category,
        detected_at_after=detected_at_after,
        detected_at_before=detected_at_before,
        app_ids=app_ids,
        scope_categories=scope_categories,
        install_state=install_state,
        count_total=count_total,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, str] = UNSET,
    offset: Union[Unset, str] = UNSET,
    classification: Union[Unset, str] = UNSET,
    vendor: Union[Unset, str] = UNSET,
    app_category: Union[Unset, str] = UNSET,
    detected_at_after: Union[Unset, str] = UNSET,
    detected_at_before: Union[Unset, str] = UNSET,
    app_ids: Union[Unset, str] = UNSET,
    scope_categories: Union[Unset, str] = UNSET,
    install_state: Union[Unset, str] = UNSET,
    count_total: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        ListApplicationsResponse400,
        ListApplicationsResponse401,
        ListApplicationsResponse403,
        ListApplicationsResponse404,
        ListApplicationsResponse500,
        list["AppsCollection"],
    ]
]:
    """List Applications for the Organization

     Get all of the organization's installed applications and their current status.
    To get the uninstalled applications, use the `install_state` filter.

    Args:
        limit (Union[Unset, str]):
        offset (Union[Unset, str]):
        classification (Union[Unset, str]):
        vendor (Union[Unset, str]):
        app_category (Union[Unset, str]):
        detected_at_after (Union[Unset, str]):
        detected_at_before (Union[Unset, str]):
        app_ids (Union[Unset, str]):
        scope_categories (Union[Unset, str]):
        install_state (Union[Unset, str]):
        count_total (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ListApplicationsResponse400, ListApplicationsResponse401, ListApplicationsResponse403, ListApplicationsResponse404, ListApplicationsResponse500, list['AppsCollection']]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            classification=classification,
            vendor=vendor,
            app_category=app_category,
            detected_at_after=detected_at_after,
            detected_at_before=detected_at_before,
            app_ids=app_ids,
            scope_categories=scope_categories,
            install_state=install_state,
            count_total=count_total,
        )
    ).parsed
